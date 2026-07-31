SELECT W1.machine_id,ROUND(AVG(W2.timestamp - W1.timestamp),3)as processing_time
FROM Activity W1
JOIN Activity W2 ON W1.machine_id = W2.machine_id AND W1.process_id = W2.process_id 
WHERE W1.activity_type = "start" AND W2.activity_type = "end"
GROUP BY machine_id