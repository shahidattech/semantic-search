from sqlalchemy.orm import Session
import sqlalchemy.orm.exc as sqlExc
import app.database.schemas as model
import logging


def isTopicExistsByName(topic_name: str, db:Session):
    try:
       return True if db.query(model.Skill).filter(model.Skill.skill_name==topic_name).all() else False
    
    except sqlExc.UnmappedColumnError as UnmappedColumnError:
        logging.error("====Error in DBService::isSkillNameExists:: UnmappedColumnError===", str(UnmappedColumnError))
        raise UnmappedColumnError
    except sqlExc.ObjectDereferencedError as ObjectDereferencedError:
        logging.error("====Error in DBService::isSkillNameExists:: ObjectDereferencedError===", str(ObjectDereferencedError))
        raise ObjectDereferencedError
    except Exception as Err:
        raise Err

def create_embedding(topic_name: str, files_in_topic: str, created_by:str, tenant_id:str, db:Session):
    try:
        obj = model.Topic(
            topic_name=topic_name,
            files_in_topic=files_in_topic,
            created_by=created_by,
            tenant_id=tenant_id,
        )
        db.add(obj)
        db.commit()
        return obj.id
    
    except sqlExc.UnmappedColumnError as UnmappedColumnError: 
        logging.error("====UnmappedColumnError Error in DBService::create_embedding:: UnmappedColumnError===" + str(UnmappedColumnError))
        raise UnmappedColumnError
    except sqlExc.ObjectDereferencedError as ObjectDereferencedError:
        logging.error("====ObjectDereferencedError Error in DBService::create_embedding:: ObjectDereferencedError===" + str(ObjectDereferencedError))
        raise ObjectDereferencedError
    except Exception as Err:
        logging.error("====Error in DBService::create_embedding:===" + str(Err))
        raise Err
