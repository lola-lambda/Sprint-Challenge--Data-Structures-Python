
class Stack:
  def __init__(self):
    self.storage = []
  
  def push(self, item):
    self.storage.append(item)

  def pop(self):
    self.storage.pop()
  
  def peek(self):
    return self.storage[len(self.storage) - 1]

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(0, item)
    self.size += 1

  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop()
    else:
      return None

  def len(self):
    return self.size

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb, stack=Stack(), finished=True):
    stack.push(self.value)
    if self.left: 
      self.left.depth_first_for_each(cb, stack, False)
    if self.right: 
      self.right.depth_first_for_each(cb, stack, False)
    if finished: 
      if len(stack.storage) > 1:
        return [cb(x) for x in stack.storage[1:]] 
      else:
        return cb(stack.storage[0])

  def breadth_first_for_each(self, cb):
    queue = Queue()
    queue.enqueue(self)
    while queue.len() > 0:
      next = queue.dequeue()
      if next.left: 
        queue.enqueue(next.left)
      if next.right:
        queue.enqueue(next.right)
      cb(next.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value