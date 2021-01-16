/* code for Simmons_cipher by Raja Baidyo */

#include<bits/stdc++.h>
using namespace std;
int main(){
	map<char,int> list,cist;
	map<char,int>::iterator itr;
	fstream file;
	file.open("plain.txt",ios::in);
	if(!file){
		cout << "The plaintext file is missing" << endl;
	}
	else{
		char ch;
		while(!file.eof()){
			file>>ch;
			int temp=(int)(ch);
			if(temp>=65 && temp<=90){
				temp+=32;
			}
			if(temp>=97 && temp<=122){
				list[(char)(temp)]++;
			}
		}
	}
	int count=0;
	for(itr=list.begin();itr!=list.end();++itr){
		// cout << itr->first << ":" << itr->second << endl;
		count+=itr->second;
	}
	cout << "total count of the chars = " << count << endl;
	cout << "And the frequecy of the english alphabets are =" << endl;
	for(itr=list.begin();itr!=list.end();++itr){
		// cout << itr->first << ":" << itr->second << endl;
		cout << itr->first << ':' << (((float)(itr->second))/((float)(count)))*100 << endl;
	}




	//***************** NOW the cipher text to see the frequency distribution//
	file.open("cipher.txt",ios::in);
	if(!file){
		cout << "The ciphertext file is missing" << endl;
	}
	else{
		char ch;
		while(!file.eof()){
			file>>ch;
			int temp=(int)(ch);
			if(temp>=65 && temp<=90){
				temp+=32;
			}
			if(temp>=97 && temp<=122){
				cist[(char)(temp)]++;
			}
		}
	}
	int c_count=0;
	for(itr=cist.begin();itr!=cist.end();++itr){
		// cout << itr->first << ":" << itr->second << endl;
		c_count+=itr->second;
	}
	cout << "total count of the cipher chars = " << c_count << endl;
	for(itr=cist.begin();itr!=cist.end();++itr){
		// cout << itr->first << ":" << itr->second << endl;
		cout << itr->first << ':' << (((float)(itr->second))/((float)(c_count)))*100 << endl;
	}

}