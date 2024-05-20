import json
from pathlib import Path
from typing import List, Optional, Union
import uuid
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader


class JSONDataLoader(BaseLoader):

    def load_ship(self,data:list) -> List[Document]:
        """Load and return documents from the JSON file."""

        docs:List[Document]=[]
   
        #iterate through ship data and create a Document for each ship
        for element in data:
            name = element['name']
            text = element['description'] + ' '.join(element['amenities'])
            description = element['description']
            amenities = element['amenities']

            metadata = dict(
                shipid = element['shipid'],
                name = name,
                description = description,
                amenities = amenities
                )

            docs.append(Document(page_content=text, metadata=metadata))
    
        return docs
        
    def load_destination(self,data:list) -> List[Document]:
        """Load and return documents from the destination JSON file."""

        docs:List[Document]=[]
   
        #iterate through destination data and create a Document for each destination
        for element in data:
            
            name = element['name']
            text = element['description'] + ' '.join(element['activities'])
            location = element['location']
            description = element['description']
            activities = element['activities']

            metadata = dict(
                destinationid = element['destinationid'],
                name = name,
                location = location,
                description = description,
                activities = activities
                )

            docs.append(Document(page_content=text, metadata=metadata))
    
        return docs

    def load_incident(self,data:list) -> List[Document]:
        """Load and return documents from the incident JSON file."""

        docs:List[Document]=[]
   
        #iterate through incident data and create a Document for each incident
        for element in data:
            
            text = element['number'] + ''.join(element['description'])\
                                    + ''.join(element['close_notes'])\
                                    + ''.join(element['business_service'])\
                                    + ''.join(element['priority'])\
                                    + ''.join(element['state'])
            number          = element['number']
            businessservice = element['business_service']
            closenotes      = element['close_notes']
            description     = element['description']
            # short_description = element['short_description']
            closedAt        = element['closed_at']
            openedAt        = element['opened_at']
            company         = element['company']
            priority        = element['priority']
            resolvedAt      = element['resolved_at']
            slaDue          = element['sla_due']
            state           = element['state']
            createdOn       = element['sys_created_on']
            updatedOn       = element['sys_updated_on']
            metadata = dict(
                number = number,
                businessservice = businessservice,
                closenotes     = closenotes,
                description    = description,
                # short_description = short_description,
                closedAt  =  closedAt,
                openedAt    = openedAt,
                company     = company,
                priority    = priority,
                resolvedAt  = resolvedAt,
                slaDue      = slaDue,
                state       = state,
                createdOn   = createdOn,
                updatedOn   = updatedOn
                )

            docs.append(Document(page_content=text, metadata=metadata))
    
        return docs

    def load_request(self,data:list) -> List[Document]:
        """Load and return documents from the request JSON file."""

        docs:List[Document]=[]
   
        #iterate through request data and create a Document for each request
        for element in data:
            
            text = element['number'] + ' '.join(element['request'])\
                                    + ' '.join(element['short_description'])\
                                    + ' '.join(element['description'])\
                                    + ' '.join(element['approval'])\
                                    + ' '.join(element['description'])\
                                    + ' '.join(element['description'])\
                                    + ' '.join(element['description'])\
                                    + ' '.join(element['close_notes'])\
                                    + ' '.join(element['business_service'])\
                                    + ' '.join(element['priority'])\
                                    + ' '.join(element['state'])
            number          = element['number']
            businessservice = element['business_service']
            closenotes      = element['close_notes']
            description     = element['description']
            # short_description = element['short_description']
            closedAt        = element['closed_at']
            openedAt        = element['opened_at']
            company         = element['company']
            priority        = element['priority']
            resolvedAt      = element['resolved_at']
            slaDue          = element['sla_due']
            state           = element['state']
            createdOn       = element['sys_created_on']
            updatedOn       = element['sys_updated_on']
            metadata = dict(
                number = number,
                businessservice = businessservice,
                closenotes     = closenotes,
                description    = description,
                # short_description = short_description,
                closedAt  =  closedAt,
                openedAt    = openedAt,
                company     = company,
                priority    = priority,
                resolvedAt  = resolvedAt,
                slaDue      = slaDue,
                state       = state,
                createdOn   = createdOn,
                updatedOn   = updatedOn
                )

            docs.append(Document(page_content=text, metadata=metadata))
    
        return docs