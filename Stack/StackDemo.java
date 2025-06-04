package Stack;

import java.util.Stack;

public class StackDemo {

    public static void main(String[] args) {
        StackDemo stackDemo = new StackDemo();
        String[] tokens = {"2","-4","+"};
        System.out.println(stackDemo.evalRPN(tokens));
    }
    public int evalRPN(String[] tokens) {

        if(tokens.length == 0) return -1;

        Stack<Integer> numbersStack = new Stack<>();
        for(String operands : tokens){

            if(operands.matches(".?[0-9]+")){
                numbersStack.push(Integer.parseInt(operands));
            }else {
                int value = performOperation(operands, numbersStack);
                numbersStack.push(value);
            }
        }

        return numbersStack.isEmpty()? -1: numbersStack.peek();
    }

    private int performOperation(String typeOfOperation, Stack<Integer> numbersStack){
        if(numbersStack.isEmpty() || numbersStack.size() < 2) return -1;

        switch (typeOfOperation) {
            case "+": {
                int second = numbersStack.pop();
                int first = numbersStack.pop();
                return first + second;
            }
            case "-": {
                int second = numbersStack.pop();
                int first = numbersStack.pop();
                return first - second;
            }
            case "*": {
                int second = numbersStack.pop();
                int first = numbersStack.pop();
                return first * second;
            }
            case "/": {
                int second = numbersStack.pop();
                int first = numbersStack.pop();
                return first / second;
            }
        }
        return -1;
    }
} 