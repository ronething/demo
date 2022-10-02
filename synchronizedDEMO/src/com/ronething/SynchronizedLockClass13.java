package com.ronething;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

// 等价代码
public class SynchronizedLockClass13 {
    Lock l = new ReentrantLock();

    public synchronized void method1() {
        System.out.println("synchronized lock");
    }

    public void method2() {
        l.lock();
        try {
            System.out.println("ReentrantLock");
        } finally {
            l.unlock();
        }
    }

    public static void main(String[] args) {
        SynchronizedLockClass13 s = new SynchronizedLockClass13();
        s.method1();
        s.method2();
    }
}
