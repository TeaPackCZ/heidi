"""
  Pose - position and orientation
"""
import math

class Pose:
  def __init__( self, x=0.0, y=0.0, heading=0.0 ):
    self.x, self.y, self.heading = x, y, heading

  def __str__( self ):
    return "(%.2f, %.2f, %d)" % (self.x, self.y, math.degrees(self.heading))

  def add( self, pose ):
    x = self.x + pose.x * math.cos( self.heading ) - pose.y * math.sin( self.heading )
    y = self.y + pose.x * math.sin( self.heading ) + pose.y * math.cos( self.heading )
    heading = self.heading + pose.heading
    return Pose(x, y, heading)

  def sub( self, pose ):
    heading = self.heading - pose.heading
    dx = self.x - pose.x
    dy = self.y - pose.y
    x = dx * math.cos( -pose.heading ) - dy * math.sin( -pose.heading )
    y = dx * math.sin( -pose.heading ) + dy * math.cos( -pose.heading )
    return Pose(x, y, heading)

  def coord( self ):
    return (self.x, self.y)

  def __iter__( self ):
    return self.iterator()

  def iterator( self ):
    yield self.x
    yield self.y
    yield self.heading

