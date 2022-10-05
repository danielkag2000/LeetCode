public class Foo {
    int i = 1;
    public Foo() {
        
    }

    public async void First(Action printFirst) {
        while(i != 1);
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        i = 2;
    }

    public async void Second(Action printSecond) {
        while(i != 2);
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        i = 3;
    }

    public async void Third(Action printThird) {
        while(i != 3);
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        i = 0;
    }
}