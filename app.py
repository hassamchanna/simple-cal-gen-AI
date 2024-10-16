{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/GfIZjqZPUeRymwrfYUNJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hassamchanna/simple-cal-gen-AI/blob/main/app_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JPtqON8Up1pr"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Function to add two numbers\n",
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "# Function to subtract two numbers\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "# Function to multiply two numbers\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "# Function to divide two numbers\n",
        "def divide(x, y):\n",
        "    if y != 0:\n",
        "        return x / y\n",
        "    else:\n",
        "        return \"Cannot divide by zero!\"\n",
        "\n",
        "# Streamlit App UI\n",
        "st.title(\"Simple Calculator\")\n",
        "\n",
        "# User input for numbers\n",
        "num1 = st.number_input(\"Enter first number\", value=0.0)\n",
        "num2 = st.number_input(\"Enter second number\", value=0.0)\n",
        "\n",
        "# User selection for operation\n",
        "operation = st.selectbox(\"Select operation\", (\"Add\", \"Subtract\", \"Multiply\", \"Divide\"))\n",
        "\n",
        "# Perform calculation based on user input\n",
        "if operation == \"Add\":\n",
        "    result = add(num1, num2)\n",
        "elif operation == \"Subtract\":\n",
        "    result = subtract(num1, num2)\n",
        "elif operation == \"Multiply\":\n",
        "    result = multiply(num1, num2)\n",
        "elif operation == \"Divide\":\n",
        "    result = divide(num1, num2)\n",
        "\n",
        "# Display the result\n",
        "if st.button(\"Calculate\"):\n",
        "    st.write(f\"The result of {operation} is: {result}\")\n"
      ]
    }
  ]
}
