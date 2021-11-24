import java.io.*;
public class Calculating_Function_486A 
{
	public static void main(String argsp[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		long n=0;
		n=Long.parseLong(br.readLine());
		long sum=0;
		
		if (n%2 == 0)
			sum = n/2;
		else
			sum = (-1)*(n/2 + 1);
		
		System.out.println(sum);

	}

}

// #800
