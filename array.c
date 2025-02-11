#include <stdio.h>
int main()

{
int a[20], i, max, min, P1, P2, n;
printf("Enter the array size: ");
scanf("%d",&n);
printf("Enter the elements: ");
for (i=0;i<n;i++)
	{
	scanf("%d",&a[i]);
	}
for(i=0;i<n;i++)
	{
	printf("%d\t",a[i]);
	}
	max=a[0];
	min=a[0];
for(i=1;i<n;i++)
	{
	if(a[i]>max)
		{
		max=a[i];
		P1=i;
		}
	if(a[i]<min)
		{
		min=a[i];
		P2=i;
		}
	}
printf("\nmax in %d in at position %d", max, P1);
printf("\nmin in %d in at position %d\n", min, P2);
return 0;
}



