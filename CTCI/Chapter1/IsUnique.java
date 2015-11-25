/*determine if a string has all unique characters. Cannot use additional data structure*/
import java.util.Scanner;

public class IsUnique {

    public static void main(String[] args) {
    	// o(n^2) time
    	// o(1) space
		Scanner input = new Scanner(System.in);
		System.out.print("Enter string: ");
		String string = input.nextLine();
		boolean unique = true;
		input.close();
		for (int i = 0; i < string.length()-1; i++){
			for (int j = i+1; j < string.length();j++){
				if(string.charAt(j) == string.charAt(i)) unique = false;
			}
		}

		if(unique) 
			System.out.println("The string contains all unique characters");
		else
			System.out.println("The string contains repeated characters");


	}
}