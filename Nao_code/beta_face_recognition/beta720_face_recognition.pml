<?xml version="1.0" encoding="UTF-8" ?>
<Package name="beta720_face_recognition" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="test625_face_recognition" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="askName" src="askName/askName.dlg" />
        <Dialog name="startFaceRecog" src="startFaceRecog/startFaceRecog.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="askName_enu" src="askName/askName_enu.top" topicName="askName" language="en_US" nuance="enu" />
        <Topic name="startFaceRecog_enu" src="startFaceRecog/startFaceRecog_enu.top" topicName="startFaceRecog" language="en_US" nuance="enu" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
