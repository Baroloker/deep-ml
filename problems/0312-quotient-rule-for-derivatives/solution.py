import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    c = 0
    function = x ** 2 + x + c
    d_function = 2 * x + c

    g_c = [0] * (3 - len(g_coeffs)) + g_coeffs
    h_c = [0] * (3 - len(h_coeffs)) + h_coeffs

    g = g_c[0] * x ** 2 + g_c[1] * x + g_c[2]
    h = h_c[0] * x ** 2 + h_c[1] * x + h_c[2]
    dg = g_c[0] * 2 * x + g_c[1]
    dh = h_c[0] * 2 * x + h_c[1]
    
    return (dg * h - g * dh) / (h ** 2)
