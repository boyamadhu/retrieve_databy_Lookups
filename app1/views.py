from django.shortcuts import render
from app1.models import *
# Create your views here.
from django.db.models import Q
def display(request):
    TO=emp.objects.all()
    TO=emp.objects.filter(ename='ALLEN')
    TO=emp.objects.exclude(ename='ALLEN')
    # FIELD LOOKUPS
    TO=emp.objects.filter(hiredate__gt='1981-04-01')
    TO=emp.objects.filter(hiredate__gte='1981-02-01')
    TO=emp.objects.filter(hiredate__lt='1981-02-01')
    TO=emp.objects.filter(hiredate__lte='1981-04-01')
    TO=emp.objects.filter(hiredate__gt='1981-04-01')
    # DATE LOOKUPS
    TO=emp.objects.filter(hiredate__year='1981')
    TO=emp.objects.filter(hiredate__month='02')
    TO=emp.objects.filter(hiredate__day='17')
    TO=emp.objects.filter(hiredate__year__gt='1980')
    TO=emp.objects.filter(hiredate__year__gte='1980')
    TO=emp.objects.filter(hiredate__year__lt='1981')
    TO=emp.objects.filter(hiredate__year__lte='1980')
    TO=emp.objects.filter(hiredate__month__gt='02')
    TO=emp.objects.filter(hiredate__day__lt='20')
    # LIKE OPERATORS
    TO=emp.objects.filter(ename__startswith='A')
    TO=emp.objects.filter(ename__endswith='h')
    # contains operator
    TO=emp.objects.filter(ename__contains='A')
    TO=emp.objects.filter(hiredate__contains='02')
    TO=emp.objects.filter(empno__contains='5')
    # IN operator
    TO=emp.objects.filter(ename__in=('smith',))
    TO=emp.objects.filter(deptno__in=('10','20'))
    # REGEX 
    TO=emp.objects.filter(ename__regex=r'[A-Z]\w{5}')
    d={'display':TO}

    return render(request,'first.html',d)

def display_dept(request):
    TO=dept.objects.all()
    d={'display':TO}


    return render(request,'second.html',d)