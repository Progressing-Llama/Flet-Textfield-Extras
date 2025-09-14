import 'dart:math';

import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

import 'flet_textfield_extras.dart';
import 'package:flet/src/flet_app_services.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "flet_textfield_extras":
      return FletTextfieldExtrasControl(
        parent: args.parent,
        control: args.control,
        children: args.children,
        parentDisabled: args.parentDisabled,
        parentAdaptive: args.parentAdaptive,
        backend: args.backend
      );
    default:
      return null;
  }
};


Widget baseControl(
    BuildContext context, Widget widget, Control? parent, Control control) {
  return _expandable(
      _directionality(
          _tooltip(
            _opacity(context, widget, parent, control),
            Theme.of(context),
            parent,
            control,
          ),
          parent,
          control),
      parent,
      control);
}

Widget constrainedControl(
    BuildContext context, Widget widget, Control? parent, Control control) {
  return _expandable(
      _badge(
          _positionedControl(
              context,
              _aspectRatio(
                  _offsetControl(
                      context,
                      _scaledControl(
                          context,
                          _rotatedControl(
                              context,
                              _sizedControl(
                                  _directionality(
                                      _tooltip(
                                          _opacity(
                                              context, widget, parent, control),
                                          Theme.of(context),
                                          parent,
                                          control),
                                      parent,
                                      control),
                                  parent,
                                  control),
                              parent,
                              control),
                          parent,
                          control),
                      parent,
                      control),
                  parent,
                  control),
              parent,
              control),
          Theme.of(context),
          parent,
          control),
      parent,
      control);
}

Widget _opacity(
    BuildContext context, Widget widget, Control? parent, Control control) {
  var opacity = control.attrDouble("opacity");
  var animation = parseAnimation(control, "animateOpacity");
  if (animation != null) {
    return AnimatedOpacity(
      duration: animation.duration,
      curve: animation.curve,
      opacity: opacity ?? 1.0,
      onEnd: control.attrBool("onAnimationEnd", false)!
          ? () {
        FletAppServices.of(context)
            .server
            .triggerControlEvent(control.id, "animation_end", "opacity");
      }
          : null,
      child: widget,
    );
  } else if (opacity != null) {
    return Opacity(
      opacity: opacity,
      child: widget,
    );
  }
  return widget;
}

Widget _tooltip(
    Widget widget, ThemeData theme, Control? parent, Control control) {
  var tooltip = parseTooltip(control, "tooltip", widget, theme);
  return tooltip ?? widget;
}

Widget _badge(
    Widget widget, ThemeData theme, Control? parent, Control control) {
  var badge = parseBadge(control, "badge", widget, theme);
  return badge ?? widget;
}

Widget _aspectRatio(Widget widget, Control? parent, Control control) {
  var aspectRatio = control.attrDouble("aspectRatio");
  return aspectRatio != null
      ? AspectRatio(
    aspectRatio: aspectRatio,
    child: widget,
  )
      : widget;
}

Widget _rotatedControl(
    BuildContext context, Widget widget, Control? parent, Control control) {
  var rotationDetails = parseRotate(control, "rotate");
  var animation = parseAnimation(control, "animateRotation");
  if (animation != null) {
    return AnimatedRotation(
        turns: rotationDetails != null ? rotationDetails.angle / (2 * pi) : 0,
        alignment: rotationDetails?.alignment ?? Alignment.center,
        duration: animation.duration,
        curve: animation.curve,
        onEnd: control.attrBool("onAnimationEnd", false)!
            ? () {
          FletAppServices.of(context).server.triggerControlEvent(
              control.id, "animation_end", "rotation");
        }
            : null,
        child: widget);
  } else if (rotationDetails != null) {
    return Transform.rotate(
        angle: rotationDetails.angle,
        alignment: rotationDetails.alignment,
        child: widget);
  }
  return widget;
}

Widget _scaledControl(
    BuildContext context, Widget widget, Control? parent, Control control) {
  var scaleDetails = parseScale(control, "scale");
  var animation = parseAnimation(control, "animateScale");
  if (animation != null) {
    return AnimatedScale(
        scale: scaleDetails?.scale ?? 1.0,
        alignment: scaleDetails?.alignment ?? Alignment.center,
        duration: animation.duration,
        curve: animation.curve,
        onEnd: control.attrBool("onAnimationEnd", false)!
            ? () {
          FletAppServices.of(context)
              .server
              .triggerControlEvent(control.id, "animation_end", "scale");
        }
            : null,
        child: widget);
  } else if (scaleDetails != null) {
    return Transform.scale(
        scale: scaleDetails.scale,
        scaleX: scaleDetails.scaleX,
        scaleY: scaleDetails.scaleY,
        alignment: scaleDetails.alignment,
        child: widget);
  }
  return widget;
}

Widget _offsetControl(
    BuildContext context, Widget widget, Control? parent, Control control) {
  var offset = parseOffset(control, "offset");
  var animation = parseAnimation(control, "animateOffset");
  if (offset != null && animation != null) {
    return AnimatedSlide(
        offset: offset,
        duration: animation.duration,
        curve: animation.curve,
        onEnd: control.attrBool("onAnimationEnd", false)!
            ? () {
          FletAppServices.of(context)
              .server
              .triggerControlEvent(control.id, "animation_end", "offset");
        }
            : null,
        child: widget);
  } else if (offset != null) {
    return FractionalTranslation(translation: offset, child: widget);
  }
  return widget;
}

Widget _positionedControl(
    BuildContext context, Widget widget, Control? parent, Control control) {
  var left = control.attrDouble("left", null);
  var top = control.attrDouble("top", null);
  var right = control.attrDouble("right", null);
  var bottom = control.attrDouble("bottom", null);

  var animation = parseAnimation(control, "animatePosition");
  if (animation != null) {
    if (left == null && top == null && right == null && bottom == null) {
      left = 0;
      top = 0;
    }

    return AnimatedPositioned(
      duration: animation.duration,
      curve: animation.curve,
      left: left,
      top: top,
      right: right,
      bottom: bottom,
      onEnd: control.attrBool("onAnimationEnd", false)!
          ? () {
        FletAppServices.of(context)
            .server
            .triggerControlEvent(control.id, "animation_end", "position");
      }
          : null,
      child: widget,
    );
  } else if (left != null || top != null || right != null || bottom != null) {
    if (parent?.type != "stack" && parent?.type != "page") {
      return ErrorControl("Error displaying ${control.type}",
          description:
          "Control can be positioned absolutely with \"left\", \"top\", \"right\" and \"bottom\" properties inside Stack control only.");
    }
    return Positioned(
      left: left,
      top: top,
      right: right,
      bottom: bottom,
      child: widget,
    );
  }
  return widget;
}

Widget _sizedControl(Widget widget, Control? parent, Control control) {
  var width = control.attrDouble("width");
  var height = control.attrDouble("height");
  if ((width != null || height != null) &&
      !["container", "image"].contains(control.type)) {
    widget = ConstrainedBox(
      constraints: BoxConstraints.tightFor(width: width, height: height),
      child: widget,
    );
  }
  var animation = parseAnimation(control, "animateSize");
  if (animation != null) {
    return AnimatedSize(
        duration: animation.duration, curve: animation.curve, child: widget);
  }
  return widget;
}

Widget _expandable(Widget widget, Control? parent, Control control) {
  if (parent != null && ["view", "column", "row"].contains(parent.type)) {
    int? expand = control.attrInt("expand");
    var expandLoose = control.attrBool("expandLoose");
    return expand != null
        ? (expandLoose == true)
        ? Flexible(flex: expand, child: widget)
        : Expanded(flex: expand, child: widget)
        : widget;
  }
  return widget;
}

Widget _directionality(Widget widget, Control? parent, Control control) {
  bool rtl = control.attrBool("rtl", false)!;
  return rtl
      ? Directionality(textDirection: TextDirection.rtl, child: widget)
      : widget;
}

void ensureInitialized() {
  // nothing to initialize
}
