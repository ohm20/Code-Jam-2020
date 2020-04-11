#include<bits/stdc++.h>
using namespace std;

struct data
{
  bool operator()( const pair<int,pair<int,int>>&d1,const pair<int,pair<int,int>>&d2)
  {
    return(d1.second<d2.second);
  }
};

int main()
{
	int t;
  cin >> t;
  int n;
  int k;
  int flag=0;
  int i;
  int s,e;
  int lc,lj;
	for(k=1;k<=t;k++)
  {
    flag=0;
    cin>>n;
    char b[n];
	  vector<pair<int,pair<int,int>>>v;
	  for(i=0;i<n;i++)
    {
      cin>>s>>e;
	    v.push_back(make_pair(i,make_pair(s,e)));
	  }

	  sort(v.begin(),v.end(),data());

    lj=0;
    lc=v[0].second.second;
    b[v[0].first]='C';

    for(i=1;i<n;i++)
    {
	    if(v[i].second.first>=lc)
      {
	      b[v[i].first]='C';
        lc=v[i].second.second;
      }
      else if(v[i].second.first>=lj)
      {
        b[v[i].first]='J';
        lj=v[i].second.second;
      }
      else
      {
        flag=1;
        break;
      }
    }
    if(flag==1)
    cout<<"Case #"<<k<<": IMPOSSIBLE";
    else
    {
      cout<<"Case #"<<k<<": ";
      for(i=0;i<n;i++)
      cout<<b[i];
    }
    cout<<endl;
  }
}