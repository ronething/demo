package com.ronething;

public class SynchronizedSuperClass12 {
    public synchronized void doSomething() {
        System.out.println("我是父类方法");
    }
}

class Testclass extends SynchronizedSuperClass12 {
    public synchronized void doSomething() {
        System.out.println("我是子类方法");
        super.doSomething();
    }

    public static void main(String[] args) {
        Testclass t = new Testclass();
        t.doSomething();
    }
}