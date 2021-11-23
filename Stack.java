public class Stack  {
    private int arr[];
    private int top;
    private int capacity;
 
    Stack(int size) {
        arr = new int[size];
        capacity = size;
        top = -1;
    }
 
    public void push(int x) {
        if (isFull()) {
            System.out.println("Overflow\nProgram Terminated\n");
            System.exit(1);
        }
        arr[++top] = x;
    }
 
    public int pop() {
        if (isEmpty()) {
            System.out.println("Underflow\nProgram Terminated");
            System.exit(1);
        }
        return arr[top--];
    }
    
    public void print() {
        for(int i = 0; i <= top; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
 
    public int peek() {
        if (!isEmpty())
            return arr[top];
        else
            System.exit(1);
 
        return -1;
    }
 
    public int size() {
        return top + 1;
    }
 
    public Boolean isEmpty() {
        return top == -1;
    }
 
    public Boolean isFull() {
        return top == capacity - 1;
    }
    
    public int elem(int elem) {
        return arr[elem];
    }

    public void search(int elem) {
        for(int i = 0; i <= top; i++) {
            if(elem == arr[i]) {
                System.out.println("Element " + elem + " found");
                return;
            }
        }
        System.out.println("Element " + elem + " not found");
    }
    public static void main(String []args) {
        Stack stack = new Stack(5);


        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);

        stack.print();
        stack.pop();
        stack.print();

        System.out.println("\nElement with index " + 0 + ": " + stack.elem(0));
        stack.search(3);
        stack.search(6);
    }
}
