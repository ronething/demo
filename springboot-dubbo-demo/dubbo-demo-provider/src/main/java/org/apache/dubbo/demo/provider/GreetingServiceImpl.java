package org.apache.dubbo.demo.provider;

import com.alibaba.dubbo.config.annotation.Service;
import org.apache.dubbo.demo.GreetingService;

@Service
public class GreetingServiceImpl implements GreetingService {
    @Override
    public String sayHello(String name) {
        return "Hello " + name + "(from Spring Boot)";
    }
}
