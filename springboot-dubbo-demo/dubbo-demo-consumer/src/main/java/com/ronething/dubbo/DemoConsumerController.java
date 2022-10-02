package com.ronething.dubbo;

import com.alibaba.dubbo.config.annotation.Reference;
import org.apache.dubbo.demo.GreetingService;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoConsumerController {

    @Reference
    private GreetingService greetingService;

    @RequestMapping("/sayHello")
    public String sayHello(@RequestParam String name) {
        return greetingService.sayHello(name);
    }

}