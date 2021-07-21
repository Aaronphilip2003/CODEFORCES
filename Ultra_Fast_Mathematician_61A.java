import java.io.*;
public class Ultra_Fast_Mathematician_61A 
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String number1="";
		String number2="";
		number1=br.readLine();
		number2=br.readLine();
		
		for(int i=0;i<number1.length();i++)
		{
			char ch1=number1.charAt(i);
			char ch2=number2.charAt(i);
			if(ch1==ch2)
				System.out.print("0");
			else
				System.out.print("1");
		}
		
		
	}

}
