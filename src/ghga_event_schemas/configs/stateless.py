# Copyright 2021 - 2024 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Config classes for stateless events"""

from pydantic import Field
from pydantic_settings import BaseSettings


class FileMetadataEventsTopic(BaseSettings):
    """For events related to new file metadata arrivals"""

    file_metadata_event_topic: str = Field(
        default=...,
        description=(
            "Name of the topic to receive new or changed metadata on files that shall"
            + " be registered for uploaded."
        ),
        examples=["metadata"],
    )
    file_metadata_event_type: str = Field(
        default=...,
        description=(
            "The type used for events to receive new or changed metadata on files that"
            + " are expected to be uploaded."
        ),
        examples=["file_metadata_upserted"],
    )


class FileUploadReceivedEventsConfig(BaseSettings):
    """For events about new file uploads"""

    file_upload_received_topic: str = Field(
        default=...,
        description="The name of the topic used for FileUploadReceived events.",
        examples=["received-file-uploads"],
    )
    file_upload_received_event_type: str = Field(
        default=...,
        description="The name of the type used for FileUploadReceived events.",
        examples=["file_upload_received"],
    )


class NotificationEventsConfig(BaseSettings):
    """For notification events."""

    notification_event_topic: str = Field(
        default=...,
        description=("Name of the topic used for notification events."),
        examples=["notifications"],
    )
    notification_event_type: str = Field(
        default=...,
        description=("The type used for notification events."),
        examples=["notification"],
    )


class FileStagingRequestedEventsConfig(BaseSettings):
    """For events that indicate a file was requested for download but not present in the outbox"""

    files_to_stage_event_topic: str = Field(
        default=...,
        description=(
            "Name of the topic used for events indicating that a download was requested"
            + " for a file that is not yet available in the outbox."
        ),
        examples=["file-downloads", "file-stage-requests"],
    )
    files_to_stage_event_type: str = Field(
        default=...,
        description="The type used for non-staged file request events",
        examples=["non_staged_file_requested"],
    )


class FileStagedEventsConfig(BaseSettings):
    """For events indicating that a file was staged to the download bucket"""

    file_staged_event_topic: str = Field(
        ...,
        description="Name of the topic used for events indicating that a new file has"
        + " been internally registered.",
        examples=["file-stagings"],
    )
    file_staged_event_type: str = Field(
        ...,
        description="The type used for events indicating that a new file has"
        + " been internally registered.",
        examples=["file_staged_for_download"],
    )


class DownloadServedEventsConfig(BaseSettings):
    """For events indicating that a file was downloaded."""

    download_served_event_topic: str = Field(
        default=...,
        description=(
            "Name of the topic used for events indicating that a download of a"
            + " specified file happened."
        ),
        examples=["file-downloads"],
    )
    download_served_event_type: str = Field(
        default=...,
        description=(
            "The type used for event indicating that a download of a specified"
            + " file happened."
        ),
        examples=["download_served"],
    )


class FileDeletionRequestEventsConfig(BaseSettings):
    """For events that require deleting a file."""

    files_to_delete_topic: str = Field(
        default=...,
        description="The name of the topic to receive events informing about files to delete.",
        examples=["file-deletion-requests"],
    )
    file_deletion_request_event_topic: str = Field(
        default=...,
        description="The type used for events indicating that a request to delete"
        + " a file has been received.",
        examples=["file_deletion_requested"],
    )


class FileDeletedEventsConfig(BaseSettings):
    """For events indicating that a given file has been deleted successfully."""

    file_deleted_event_topic: str = Field(
        default=...,
        description="Name of the topic used for events indicating that a file has"
        + " been deleted.",
        examples=["file-deletions"],
    )
    file_deleted_event_type: str = Field(
        default=...,
        description="The type used for events indicating that a file has"
        + " been deleted.",
        examples=["file_deleted"],
    )


class _FileInterrogationsConfig(BaseSettings):
    file_interrogations_topic: str = Field(
        default=...,
        description=(
            "The name of the topic use to publish file interrogation outcome events."
        ),
        examples=["file-interrogations"],
    )


class FileValidationSuccessEventsConfig(_FileInterrogationsConfig):
    """For events conveying that a file interrogation was successful"""

    interrogation_success_event_type: str = Field(
        default=...,
        description=(
            "The type used for events informing about successful file validations."
        ),
        examples=["file_interrogation_success"],
    )


class FileValidationFailureEventsConfig(_FileInterrogationsConfig):
    """For events conveying that a file interrogation was unsuccessful"""

    interrogation_failure_event_type: str = Field(
        default=...,
        description=(
            "The type used for events informing about failed file validations."
        ),
        examples=["file_interrogation_failed"],
    )


class FileToRegisterEventsConfig(BaseSettings):
    """For events containing info about a file to register"""

    files_to_register_event_topic: str = Field(
        default=...,
        description="The name of the topic to receive events informing about new files "
        + "to register.",
        examples=["files-to-register"],
    )
    files_to_register_event_type: str = Field(
        default=...,
        description="The name of the type for events informing about new files "
        + "to register.",
        examples=["file_to_register"],
    )


class FileRegisteredEventsConfig(BaseSettings):
    """For events conveying that a file was registered in the permanent bucket."""

    file_registered_event_topic: str = Field(
        default=...,
        description=(
            "Name of the topic used for events indicating that a file has"
            + " been registered for download."
        ),
        examples=["file-registrations"],
    )
    file_registered_event_type: str = Field(
        default=...,
        description=(
            "The type used for event indicating that that a file has"
            + " been registered for download."
        ),
        examples=["file_registered"],
    )


class _AccessRequestConfig(BaseSettings):
    access_request_events_topic: str = Field(
        default=...,
        description="Name of the event topic used to consume access request events",
        examples=["access-requests"],
    )


class AccessRequestCreatedEventsConfig(_AccessRequestConfig):
    """For events conveying an access request was created"""

    access_request_created_event_type: str = Field(
        default=...,
        description="The type to use for access request created events",
        examples=["access_request_created"],
    )


class AccessRequestAllowedEventsConfig(_AccessRequestConfig):
    """For events conveying an access request was allowed/approved"""

    access_request_allowed_event_type: str = Field(
        default=...,
        description="The type to use for access request allowed events",
        examples=["access_request_allowed"],
    )


class AccessRequestDeniedEventsConfig(_AccessRequestConfig):
    """For events conveying an access request was denied"""

    access_request_denied_event_type: str = Field(
        default=...,
        description="The type to use for access request denied events",
        examples=["access_request_denied"],
    )


class IvaChangeEventsType(BaseSettings):
    """For events communicating updates to IVA statuses.

    This is not for stateful event communication, despite the name.
    """

    iva_state_changed_event_topic: str = Field(
        default=...,
        description="The name of the topic containing IVA events.",
        examples=["ivas"],
    )
    iva_state_changed_event_type: str = Field(
        default=...,
        description="The type to use for iva state changed events.",
        examples=["iva_state_changed"],
    )


class _AuthEventsConfig(BaseSettings):
    auth_event_topic: str = Field(
        default=...,
        description="The name of the topic containing auth-related events.",
        examples=["auth-events"],
    )


class SecondFactorRecreatedEventsConfig(_AuthEventsConfig):
    """For events conveying that 2nd auth factor has been recreated"""

    second_factor_recreated_event_type: str = Field(
        default=...,
        description="The event type for recreation of the second factor for authentication",
        examples=["second_factor_recreated"],
    )
