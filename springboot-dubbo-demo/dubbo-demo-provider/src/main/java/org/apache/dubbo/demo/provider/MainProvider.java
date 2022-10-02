package org.apache.dubbo.demo.provider;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.support.ClassPathXmlApplicationContext;

@SpringBootApplication
public class MainProvider {
    public static void main(String[] args) {
        SpringApplication.run(MainProvider.class,args);
    }
}