# [Silver II] 골드바흐의 추측 - 9020 

[문제 링크](https://www.acmicpc.net/problem/9020) 

### 성능 요약

메모리: 33376 KB, 시간: 2040 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 문제 설명

<p>A natural number is called a prime number (or a prime) if it is bigger than 1 and has no divisors other than 1 and itself. For example, 5 is prime, since no number except 1 and 5 divides it. On the other hand, 6 is not a prime since 6 = 2 × 3 . </p>

<p>Goldbach's conjecture is one of the famous unsolved problems in number theory and in all of mathematics. It states: Every even integer greater than 2 can be expressed as the sum of two primes. Such a number is called a Goldbach number. Expressing a given even number as a sum of two primes is called a Goldbach partition of the number. For example, 4 = 2 + 2 , 6 = 3 + 3 , 8 = 3 + 5 , 10 = 7 + 3 or 10 = 5 + 5 , 12 = 5 + 7 , 14 = 3 + 11 or 14 = 7 + 7 . Note that Goldbach partition has been found for any even interger n less than 10000.</p>

<p>Given any even integer n greater than 2, write a program that prints the two primes of the Goldbach partition of n . If there are more than one Goldbach partitions of n, find a partition such that the difference of the two primes of it is minimized. </p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case consists of an even integer n (4 ≤ n ≤ 10,000 ) .</p>

### 출력 

 <p>Your program is to write to standard output. For each test case, find the Goldbach partition as described above, and print its two primes in non-decreasing order with one blank between them.</p>

