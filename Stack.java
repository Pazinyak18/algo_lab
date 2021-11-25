public class Stack {
    private int size;
    private Node top = null;

    public static void main(String[] args) {
        Stack stack = new Stack();

        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);

        stack.print();
        stack.pop();
        stack.print();

        System.out.println(stack.getElem(2));
    }

    public void push(int x) {
        Node nodeToPut = new Node(x);
        nodeToPut.pointer = top;
        top = nodeToPut;
        size++;
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }
        Node temp = top;
        top = top.pointer;
        return temp.value;
    }

    public void print() {
        if (isEmpty()) {
            System.out.println("No elem to print");
            return;
        }
        Node iterator = top;
        while (iterator != null) {
            System.out.println("[" + iterator.getValue() + "]");
            iterator = iterator.pointer;
        }
        System.out.println();
    }

    public int peek() {
        if (isEmpty()) {
            return -1;
        }
        return top.value;
    }

    public int getSize() {
        return size;
    }

    public Boolean isEmpty() {
        return top == null;
    }

    public int getElem(int valueToSearch) {
        if (isEmpty()) {
            System.out.println("No elem to search");
            return -1;
        }
        Node iterator = top;
        while (iterator.pointer != null) {
            if (iterator.value == valueToSearch) {
                return iterator.value;
            }
            iterator = iterator.pointer;
        }
        return -1;
    }

    class Node {
        private Node pointer = null;
        private int value;

        Node(int val) {
            value = val;
        }

        public Node getPointer() {
            return pointer;
        }

        public void setPointer(Node pointer) {
            this.pointer = pointer;
        }

        public int getValue() {
            return value;
        }

        public void setValue(int value) {
            this.value = value;
        }
    }
}