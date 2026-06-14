def log_arguments(func):
    def wrapper(*args, **kwargs):
        from time import ctime
        
        res = func(*args, **kwargs)
        func_name = str(func).split(' ')[1]
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join(map(str, kwargs))
        with open("log.txt", "a", encoding="utf-8") as f:
            print(f"[{ctime()}]"
                  f" Виклик функції {func_name}" \
                  f" з аргументами ({args_str})" \
                  f" та іменованими аргументами ({kwargs_str})." \
                  f" Результат: {res}.",
                  file=f)
        
        return res
    
    return wrapper


@log_arguments
def print_sum(*args):
    print(sum(args))
    
@log_arguments
def get_sum(*args):
    return sum(args)

@log_arguments
def get_list_args_and_kwargs(*args, **kwargs):
    return list(args) + list(kwargs.items())





def check_access(password):
    def decorator_wrapper(func):
        def wrapper(*args, **kwargs):
            import os
            
            if password == os.getenv("SECRET_KEY"):
                res = func(*args, **kwargs)
                return res
            else:
                raise PermissionError("Доступ заборонено! Невірний ключ.")
            
        return wrapper
    return decorator_wrapper
        
        
@check_access("admin123")
def get_admin_email():
    return "admin@project.com"


def main():
    # 1
    print_sum(1,2,3,4)
    print(get_sum(10, 20))
    print(get_list_args_and_kwargs(1,4, 'apole', 'nine', {'stop', 2}, name='Ivan'))

    # 2
    import os
    try:
        os.environ["SECRET_KEY"] = "admin123"
        print(get_admin_email())
        print("Міняю пароль...")
        os.environ["SECRET_KEY"] = "qwerty"
        print(get_admin_email())
    except Exception as e:
        print(e)
    
    

if __name__ == "__main__":
    main()
