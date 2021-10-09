#include<iostream>
#include<cmath>
#include<string>
using namespace std;
int main()
{
   string a,b;
   int c=10,d=4;
   bool f=true;
   cout<<"enter 1st name "<<"and second name";
   cin>>a>>b;
   cout<<"length of the string: "<<a.length();
   cout<<b.append(a);
   cout<<"\n"<<b[7];
   cin>>b[2];
   cout<<a<<"\n";
   cout<<b;
   cout<<"\n"<<max(c,d)<<"\n"<<f;
   cout<<(c==d);
   string result = (c>d)?"good mornig":"good night";
   cout<<"\n"<<result;

}
