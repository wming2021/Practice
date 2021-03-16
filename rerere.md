1.py  装饰器

    装饰器

2.py  继续加油 
    
    王美儿 必胜
3.py

    提交代码时，偶尔会出现提交失败的情况，并提示：OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443

    原因：
        是Git的Http代理的问题，Git支持三种协议：git://、ssh:// 和 http://，本来push的时候应该走ssh隧道的，但是因为设置了http代理，所以就走了http的代理，于是就提交不了了。
    解决方法是：
        git config --global --unset http.proxy
    链接：
        https://blog.csdn.net/weixin_42125310/article/details/106212710