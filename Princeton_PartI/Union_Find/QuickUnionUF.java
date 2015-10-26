public class QuickUnionUF{
	private int[] id;

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
	  logic: connect two points by setting the root of the first point
	  	to be the root of the second point. 
	*/
	public void union(int p, int q){
		int i = root(p);
		int j = root(q);
		id[i] = j
	}
}