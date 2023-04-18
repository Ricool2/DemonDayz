extends KinematicBody2D

var velocity = Vector2.ZERO
const speed = 100
const acceleration = 300
const friction = 500

onready var animationPlayer = $AnimationPlayer
onready var animationTree = $AnimationTree
onready var sprite = $Sprite
onready var animationState = animationTree.get('parameters/playback')

func _ready():
	animationTree.active = true

#func _process(delta):
#	pass

func _physics_process(delta):
	var input_vector = Vector2.ZERO
	
	input_vector.x = Input.get_action_raw_strength("move_right") - Input.get_action_raw_strength("move_left")
	input_vector.y = Input.get_action_raw_strength("move_down") - Input.get_action_raw_strength("move_up")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		animationTree.set('parameters/Idle/blend_position', input_vector)
		animationTree.set('parameters/Move/blend_position', input_vector)
		if input_vector.x < 0:
			sprite.flip_h = true
#			animationPlayer.advance(0)
		else:
			sprite.flip_h = false
		animationState.travel("Move")
		velocity = velocity.move_toward(input_vector * speed, acceleration * delta)
	else:
		animationState.travel("Idle")
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)

	velocity = move_and_slide(velocity)
