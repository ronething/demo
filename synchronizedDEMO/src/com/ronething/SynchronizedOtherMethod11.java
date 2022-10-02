package com.ronething;

public class SynchronizedOtherMethod11 {
    public synchronized void method1(){
        System.out.println("i am method1");
        method2();
    }

    public synchronized void method2(){
        System.out.println("i am method2");
    }

    public static void main(String[] args) {
        SynchronizedOtherMethod11 s = new SynchronizedOtherMethod11();
        s.method1();
    }
}
