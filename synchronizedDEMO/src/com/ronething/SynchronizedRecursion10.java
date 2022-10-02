package com.ronething;

public class SynchronizedRecursion10 {
    static SynchronizedRecursion10 instance = new SynchronizedRecursion10();
    static int i = 0;

    public static void main(String[] args) {
        instance.method();
    }

    private synchronized void method() {
        System.out.println("i is " + i);
        if (i == 0) {
            i++;
            method();
        }
    }
}

