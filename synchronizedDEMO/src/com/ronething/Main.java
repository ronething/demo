package com.ronething;

public class Main implements Runnable {

    static Main instance = new Main();

    static int i = 0;

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(instance);
        Thread t2 = new Thread(instance);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println(i);
    }

    @Override
    public void run() {
        synchronized (this) {
            for (int j = 0; j < 100000; j++) {
                i++;
            }
        }
    }
}
