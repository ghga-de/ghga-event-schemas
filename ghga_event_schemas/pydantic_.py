# Copyright 2022 Universität Tübingen, DKFZ and EMBL
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

"""Contains pydantic BaseModel-based versions of the schemas.

Please note, these pydantic-based schemas are the source of thruth for all other
schema representations such as json-schema.
"""

from pydantic import BaseModel, Field


class FileUploadValidationSuccess(BaseModel):
    """Contains details for successfully checksum validated file processing"""

    file_id: str = Field(..., alias="file-id")
    secret_id: str = Field(..., alias="secret-id")
    offset: int
    part_size: int = Field(..., alias="part-size")
    part_checksums_md5: list[str] = Field(..., alias="part-checksums-md5")
    part_checksums_sha256: list[str] = Field(..., alias="part-checksums-sha256")
    content_checksum_sha256: str = Field(..., alias="sha256-checksum")

    class Config:
        """Needed config to allow popupalation by non-alias name"""

        allow_population_by_field_name = True


class FileUploadValidationFailure(BaseModel):
    """Contains details in case of file checksum validation failure"""

    file_id: str = Field(..., alias="file-id")
    cause: str

    class Config:
        """Needed config to allow popupalation by non-alias name"""

        allow_population_by_field_name = True


# Lists event schemas (values) by event types (key):
schema_registry: dict[str, type[BaseModel]] = {
    "file_upload_validation_success": FileUploadValidationSuccess,
    "file_upload_validation_failure": FileUploadValidationFailure,
}
