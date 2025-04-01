#include<stdio.h>
struct student
{
char name[20];
int roll_no;
int mark[10];
int total;
float avg;
};
int main()
{
int n,i,j;
printf("enter the no of students:\n");
scanf("%d",&n);
struct student stu[n];
for(i=0;i<n;i++)
{
printf("Name:\n");
scanf("%s",stu[i].name);
printf("Roll_no\n");
scanf("%d",&stu[i].roll_no);
stu[i].total=0;
for(j=0;j<3;j++)
{
printf("Mark:\n");
scanf("%d",&stu[i].mark[j]);
stu[i].total+=stu[i].mark[j];
}
stu[i].avg=stu[i].total/3;
printf("Total;\n");
scanf("%d",&stu[i].total);
printf("Avg:\n");
scanf("%f",&stu[i].avg);
}
return 0;
}


