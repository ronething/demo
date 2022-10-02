package com.ronething;

public class SynchronizedException9 implements Runnable {
    static SynchronizedException9 instance = new SynchronizedException9();

    public static void main(String[] args) {
        Thread t1 = new Thread(instance);
        Thread t2 = new Thread(instance);
        t1.start();
        t2.start();
        while (t1.isAlive() || t2.isAlive()) {
        }
        System.out.println("finished");
    }

    @Override
    public void run() {
        if (Thread.currentThread().getName().equals("Thread-0")) {
            method1();
        } else {
            method2();
        }
    }

    public synchronized void method1() {
        System.out.println("加锁 static 方法1, " + Thread.currentThread().getName());
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        throw new RuntimeException();
//        System.out.println(Thread.currentThread().getName() + "运行结束");
    }

    public synchronized void method2() {
        System.out.println("加锁非 static 方法2, " + Thread.currentThread().getName());
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(Thread.currentThread().getName() + "运行结束");
    }

}
