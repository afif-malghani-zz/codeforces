#include<stdio.h>

int main(){
	int probs;
	scanf("%i",&probs);
	int count = 0;
	for(int i=probs;i>0;i--){	
		int a, s, d;
		scanf("%i %i %i", &a, &s, &d);
		if(a+s+d > 1){count++;}
	}
	printf("%i",count);
	printf("\n");
	return(0);

}
