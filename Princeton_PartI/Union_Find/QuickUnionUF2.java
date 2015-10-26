/*
	A modified version of QuickUnionUF
	Trying to avoid tall trees
	Use a array to keep track the sizes of each tree
	And always link root of smaller tree to root of larger tree	
*/

public class QuickUnionUF2{

	private int[] id;
	private int[] sz;

	/*Constructor*/
	public QuickUnionUF(int N){
		id = new int[N];
		for (int i = 0; i < N; i++)
			id[i] = i;
	}

	/*
	  find the root of a given point
	  input: the index of a point
	  output: the index of the root point
	  logic: search level by level up the tree to find to root
	*/
	private int root(int i){
		while (i != id[i])
			i = id[i];
		return i;
	}

	/*
	  test if two points are conncected
	  input: the indices of two points
	  output: true if two points are connected
	  logic: if two points have the same root, they are connected
	*/
	public boolean connected(int p, int q){
		return root(p) == root(q);
	}

	/*
	  connect two points
	  input: the indices of two points
	  output: nothing
	  logic: connect two points by setting the root of the smaller size tree
	  	to be the root of the larger tree
	*/
	public void union(int p, int q){
		int i = root(p);
		int j = root(q);
		if (i == j)
			return;
		if (sz[i] < sz[j]){
			id[i] = j;
			sz[j] += size[i];
		}
		else{
			id[j] = i;
			sz[i] += size[j];
		}
	}
}