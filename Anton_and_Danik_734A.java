import java.io.*;
public class Anton_and_Danik_734A
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=0;
		String s;
		n=Integer.parseInt(br.readLine());
		s=br.readLine();
		int countA=0,countD=0;
		for(int i=0;i<s.length();i++)
		{
			char ch=s.charAt(i);
			if(ch=='A')
				countA++;
			else if(ch=='D')
				countD++;
		}
		if(countA>countD)
			System.out.println("Anton");
		else if(countD>countA)
			System.out.println("Danik");
		else
			System.out.println("Friendship");
	}

}

// 800 rated problem
