# Import the Streamlit library
import streamlit as st

# Give a title to our app
st.title('Simple Calculator')

# Get the first number from the user
num1 = st.number_input('Enter the first number')

# Get the second number from the user
num2 = st.number_input('Enter the second number')

# Drop Down Menu for Operation Selection
Operation = st.selectbox('Choose an Operation', ('Add','Subtract', 'Multiply', 'Divide'))

# Create buttons for different operations
# add = st.button('Add')
# subtract = st.button('Subtract')
# multiply = st.button('Multiply')
# divide = st.button('Divide')

# Perform calculations and display results
if Operation == 'Add':
    result = num1 + num2
    st.write('The sum is:', result)
elif Operation == 'Subtract':
    result = num1 - num2
    st.write('The subtraction is:', result)
elif Operation == 'Multiply':
    result = num1 * num2
    st.write('The multiplication is:', result)
elif Operation == 'Divide':
    if num2 != 0:
        result = num1 / num2
        st.write('The division is:', result)
    else:
        st.write('Division by zero is not allowed!')
        