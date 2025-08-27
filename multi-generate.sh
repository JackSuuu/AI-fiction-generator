NUM_OF_ITER=5  # 设置迭代次数

for ((i=1; i<=NUM_OF_ITER; i++)); do
    echo "Iteration $i of $NUM_OF_ITER"
    /Users/jacksu/Desktop/AI-auto-writer-script/.venv/bin/python auto_writer.py
done