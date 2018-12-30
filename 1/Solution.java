

public class Solution {
  public static void main(String[] args) {
    int[] providedData = new int[] {15, 3, 7, 10};
    int target = 17;

    System.out.println("Is " + target + " in the list: " + listAsString(providedData) + "? " + solution1(providedData, target));
  }

  public static boolean solution1(int[] nums, int target) {
    if(nums == null || nums.length == 1) {
      return false;
    }

    int[] differences = new int[nums.length];

    differences[0] = target - nums[0];
    for (int i = 1; i < nums.length; i++) {
      for( int j = 0; j < i; j++) {
        if (differences[j] == nums[i]) {
          return true;
        }
      }
      differences[i] = target - nums[i];
    }
    return false;
  }

  public static boolean solution2(int[] nums, int target) {
    return false;
  }

  //not relevant
  public static String listAsString(int[] vals) {
    Integer[] ints = new Integer[vals.length];
    for( int i = 0; i < vals.length; i++) {
      ints[i] = Integer.valueOf(vals[i]);
    }
    return listAsString(ints);
  }
  
  public static <T> String listAsString(T[] vals) {
    StringBuilder sb = new StringBuilder("[");

    if (vals.length > 0) {
      sb.append(vals[0]);
    }

    for(int i = 1; i < vals.length; i++) {
      sb.append(", ").append(vals[i]);
    }

    sb.append("]");
    return sb.toString();
  }
}