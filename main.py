import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


# Function to find critical points
def find_critical_points(func, var):
    # Find the first derivative
    derivative = sp.diff(func, var)

    # Find the critical points by solving derivative = 0
    critical_points = sp.solve(derivative, var)

    # Find second derivative for classifying critical points
    second_derivative = sp.diff(derivative, var)

    # Classify the critical points
    extrema = {}
    for point in critical_points:
        # Evaluate second derivative at each critical point
        concavity = second_derivative.subs(var, point)
        if concavity > 0:
            extrema[point] = 'Minima'
        elif concavity < 0:
            extrema[point] = 'Maxima'
        else:
            extrema[point] = 'Saddle point'

    return extrema


# Plotting function
def plot_function(func, var, extrema_points):
    # Convert sympy function to numpy function for plotting
    f_lambdified = sp.lambdify(var, func, 'numpy')

    # Generate x values and evaluate the function at those values
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)

    # Create plot
    plt.plot(x_vals, y_vals, label=f'f({var}) = {func}')
    plt.title(f"Graph of {func}")
    plt.xlabel(f'{var}')
    plt.ylabel(f'f({var})')

    # Highlight extrema points on the graph
    for point, point_type in extrema_points.items():
        x_point = float(point)
        y_point = f_lambdified(x_point)
        plt.scatter(x_point, y_point, color='red' if point_type == 'Maxima' else 'blue', zorder=5)
        plt.text(x_point, y_point, f'{point_type} ({point}, {y_point:.2f})')

    plt.grid(True)
    plt.legend()
    plt.show()


def display_explanations():
    print("\nDefinitions:")
    print("1. **Minima**: A point on the graph where the function changes from decreasing to increasing. It represents the lowest point in a certain interval.")
    print("2. **Maxima**: A point on the graph where the function changes from increasing to decreasing. It represents the highest point in a certain interval.")
    print("3. **Saddle Point**: A point where the function does not have a local minimum or maximum, but the slope (derivative) is zero. The function changes direction but not in a way that makes it a peak or a trough.")
    input("\nPress Enter to continue...")  # Wait for user to acknowledge the definitions


def calculate_area(func, var):
    # Ask for integration limits
    lower_limit = float(input("Enter the lower limit of integration: "))
    upper_limit = float(input("Enter the upper limit of integration: "))

    # Calculate the definite integral
    area = sp.integrate(func, (var, lower_limit, upper_limit))
    
    return area


def main():
    # Display explanations of critical points
    display_explanations()

    # Ask user for the function
    x = sp.symbols('x')
    func_input = input("Enter a function of x (e.g., x**3 - 3*x**2 + 2): ")
    func = sp.sympify(func_input)

    # Find critical points
    extrema_points = find_critical_points(func, x)

    # Display the critical points and their types
    print("Critical Points:")
    for point, point_type in extrema_points.items():
        print(f"x = {point}: {point_type}")

    # Plot the function with the extrema points highlighted
    plot_function(func, x, extrema_points)

    # Calculate the area under the curve
    area = calculate_area(func, x)
    print(f"The area under the curve from the given limits is: {area}")


if __name__ == "__main__":
    main()
