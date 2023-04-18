extends KinematicBody2D

var velocity = Vector2.ZERO
const speed = 100
const acceleration = 300
const friction = 500

onready var animationPlayer = $AnimationPlayer
onready var animationTree = $AnimationTree
onready var animationState = animationTree.get('parameters/playback')

func _ready():
	$Move.visible = false
	pass

#func _process(delta):
#	pass

func _physics_process(delta):
	var input_vector = Vector2.ZERO
	
	input_vector.x = Input.get_action_raw_strength("move_right") - Input.get_action_raw_strength("move_left")
	input_vector.y = Input.get_action_raw_strength("move_down") - Input.get_action_raw_strength("move_up")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		$Move.visible = true
		$Idle.visible = false
		animationTree.set('parameters/Idle/blend_position', input_vector)
		animationTree.set('parameters/Move/blend_position', input_vector)
		animationState.travel("Move")
		velocity = velocity.move_toward(input_vector * speed, acceleration * delta)
	else:
		$Move.visible = false
		$Idle.visible = true
		animationState.travel("Idle")
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)

	velocity = move_and_slide(velocity)
#func _physics_process(delta):
#	velocity = Vector2.ZERO
#	if Input.is_action_pressed("move_left"):
#		velocity.x -= 1
#	if Input.is_action_pressed("move_up"):
#		velocity.y -= 1
#	if Input.is_action_pressed("move_down"):
#		velocity.y += 1
#	if Input.is_action_pressed("move_right"):
#		velocity.x += 1
#
#	velocity = (velocity * delta).normalized() * speed
#	move_and_slide(velocity)
