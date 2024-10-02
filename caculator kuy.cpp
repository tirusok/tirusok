#include <iostream>
using namespace std;

int main() {
    double num1, num2, result;
    char operation;
    
    // Input
    cout << "Enter first number: ";
    cin >> num1;
    
    cout << "Enter operation (+, -, *, /): ";
    cin >> operation;
    
    cout << "Enter second number: ";
    cin >> num2;
    
    // Process (operasi)
    switch(operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if(num2 != 0) {
                result = num1 / num2;
            } else {
                cout << "Error: Division by zero!" << endl;
                return 1;
            }
            break;
        default:
            cout << "Invalid operation!" << endl;
            return 1;
    }
    
    // Output (hasil)
    cout << "Result: " << result << endl;
    
    return 0;
}