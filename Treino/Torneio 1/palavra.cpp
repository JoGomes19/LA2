#include <iostream>
#include <stdio.h>
#include <set>
#include <sstream>
#include <string>
#include <map>
#include <list>
#include <vector>
#include <queue>
#define MAXIMO 10000
#define MAXI(x,y) (x<y)?y:x
using namespace std;
void cal_m(string s)
{
	for(int i=1;i<(int)s.length();i++)
	{
		string oi=s;
		string str3= s.substr(i);
		int ina=0;
		cout<<str3<<"\n";
		int j;
		for(j=0;j<(int)str3.length();j++)
		{
			cout<<str3[j]<<" "<<s[j]<<"\n";
			if(str3[j]!=s[j])
			{
				ina=1;
				break;
			}
		}
		if(ina==0){
			for(;j<(int)s.length();j++)
				s.push_back(s[j]);		
			cout<<"PALAVRA:->"<<oi<<"\n";
		}			
	}
}
int main(){
	string s;
	while(cin>>s){
		cal_m(s);
	}
	return 0;
}
