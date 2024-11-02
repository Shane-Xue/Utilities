#ifndef BIGNUM_H
#define BIGNUM_H

#include <string>
#include <algorithm>
#include <vector>
#include <stdexcept>
#include <sstream>
#include <cstring>
#include <cctype>

#ifdef DEBUG
#include <iostream>
#endif

namespace BigNum{
	using namespace std;
	class Integer{
	private:
		vector<int> digits{}; //Big Endian
		bool negative; //Does it have a negative sign?
	public:
		Integer():digits(vector<int>{}), negative(false){};

		Integer(string s){
			if (s[0] == '-'){
				negative = true;
			}else negative = false;
			if (not isdigit(s[0]))
			{
				s = s.substr(1);
			}
			for (auto i = s.rbegin(); i != s.rend(); i++){
				digits.push_back(*i - '0');
			}
		}

		Integer(Integer& other):digits(other.digits), negative(other.negative){}

		Integer(Integer&& other){
			digits = move(other.digits);
			negative = other.negative;
			other.negative = false;
		}

		template<typename T>
		Integer(T num, enable_if_t<is_integral<T>::value, int> = 0){
			if (num < 0){
				negative = true;
				num = -num;
			}
			while(num){
				digits.push_back(num % 10);
				num /= 10;
			}
		}

		bool operator==(Integer other) const{
			return (digits == other.digits) and (negative == other.negative);
		}

		bool operator>(Integer other) const{
			if (*this == other) return false;
			if (negative != other.negative) return other.negative;
			if (digits.size() != other.digits.size()) return digits.size() > other.digits.size();
			bool abs_comp = false;
			for (int i = digits.size() - 1; i != 0; --i){
				if (digits[i] == other.digits[i]) continue;
				else{
					abs_comp = (digits[i] > other.digits[i]);
					break;
				}
			}
			return ((negative) ? (not abs_comp) : (abs_comp));
		}

		bool operator<(Integer other) const{
			return not((*this == other) or (*this > other));
		}

		bool operator<=(Integer other) const{
			return not(*this > other);
		}

		bool operator>=(Integer other) const{
			return not(*this < other);
		}

		Integer operator=(Integer& other){
			digits = other.digits;
			negative = other.negative;
			return *this;
		}

		Integer operator=(Integer&& other){
			digits = move(other.digits);
			negative = other.negative;
			other.negative = false;
			return *this;
		}

		void rectify(){
			// Does not deal with last digit
			int i = 0;

			#ifdef DEBUG
			cout << "Rectifying\n";
			#endif

			while(true){

				auto last_elem = this->digits.end();
				if (digits.begin() + i == last_elem) break;
				#ifdef DEBUG
				cout << "Current iterator distance: " << last_elem - digits.begin() + i << endl;
				cout << "Current element: " << *(digits.begin() + i) << endl;
				#endif

				//Resolve negative issue
				if (*(digits.begin() + i) < 0){
					// This should not happen on the last digit if everything goes right.
					// Negativity should be the first step of resolving issues.
					if (digits.begin() + i + 1 == last_elem){
						throw runtime_error("Negativity was not resolved beforehand.");
					}
					int borrow = abs(*(digits.begin() + i) / 10 - 1);
					*(digits.begin() + i) += borrow * 10;

					*((digits.begin() + i) + 1) -= borrow;
				}

				// resolve overflow
				if(*(digits.begin() + i) > 9){
					if ((digits.begin() + i) + 1 == last_elem and (*(digits.begin() + i) / 10)){
						this->digits.push_back(*(digits.begin() + i) / 10);
					}
					else *((digits.begin() + i) + 1) += *(digits.begin() + i) / 10;
					*(digits.begin() + i) %= 10;
				}
				i++;
			}

			while(*(digits.end() - 1)  == 0 and digits.end() - digits.begin() > 1) digits.pop_back();
		}

		Integer operator-(){
			Integer copy = *this;
			copy.negative = not copy.negative;
			return copy;
		}

		Integer operator+(Integer other){

			#ifdef DEBUG
			cout << "In function add\n";
			#endif

			if (other.negative and not this->negative) return *this - (-other);
			else if (not other.negative and this->negative) return other - (-*this);
			else if (other.negative and this->negative) return -((-other) + (-*this));
			Integer bigger, smaller;
			if (*this > other)
			{
				bigger = *this;
				smaller = other;
			}else{
				bigger = other;
				smaller = *this;
			}
			for (int i = 0; i < smaller.digits.size(); ++i)
			{
				bigger.digits[i] += smaller.digits[i];
			}
			#ifdef DEBUG
			cout << bigger;
			#endif
			bigger.rectify();
			return bigger;
		}

		Integer operator-(Integer other){
			#ifdef DEBUG
			cout << "In function minus\n";
			#endif

			if (not this->negative and other.negative) return *this + (-other);
			else if (this->negative and other.negative) return (-other) - (-*this);
			else if (this->negative and not other.negative) return -((other) + (-*this));
			Integer bigger, smaller;
			if (*this > other)
			{
				bigger = *this;
				smaller = other;
			}else{
				bigger = other;
				smaller = *this;
			}
			bool negate = (*this < other);
			for (int i = 0; i < smaller.digits.size(); ++i)
			{
				bigger.digits[i] -= smaller.digits[i];
			}
			#ifdef DEBUG
			cout << bigger;
			#endif
			bigger.rectify();
			return ((negate) ? (-bigger) : (bigger));
		}

		string str() const{
			string cache;
			stringstream parse("");
			for (auto&& i : digits){
				parse << i;
			}
			cache = parse.str();
			reverse(cache.begin(), cache.end());
			return ((negative) ? ("-") : ("")) + cache;
		}

		friend ostream& operator<<(ostream& out, const Integer i){
			out << i.str();
			return out;
		}

		~Integer(){};
	};
}

#endif