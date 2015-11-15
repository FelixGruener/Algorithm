public class Test{
	public static void main(String[] args) {

	System.out.println("Test quick-find after the following connecting: ");
	System.out.println("5-6 9-8 0-1 4-7 8-0 1-4");
	QuickFindUF UF = new QuickFindUF(10);
	UF.print();
	UF.union(5,6);
	UF.print();
	UF.union(9,8);
	UF.print();
	UF.union(0,1);
	UF.print();
	UF.union(4,7);
	UF.print();
	UF.union(8,0);
	UF.print();
	UF.union(1,4);
	UF.print();

	System.out.println("Test weighted quick-union after the following connecting: ");
	System.out.println("6-2 8-0 6-9 1-4 3-9 5-3 4-0 3-7 3-8");
	QuickUnionUF2 UF2 = new QuickUnionUF2(10);	
	UF2.print();
	UF2.union(6,2);
	UF2.print();
	UF2.union(8,0);
	UF2.print();
	UF2.union(6,9);
	UF2.print();
	UF2.union(1,4);
	UF2.print();
	UF2.union(3,9);
	UF2.print();
	UF2.union(5,3);
	UF2.print();
	UF2.union(4,0);
	UF2.print();
	UF2.union(3,7);
	UF2.print();
	UF2.union(3,8);
	UF2.print();
	}
}