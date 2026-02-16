# $NetBSD$

DISTNAME=	mlflow-3.10.0rc0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=m/mlflow/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/mlflow/
COMMENT=	open source platform for complete machine learning lifecycle
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

# build dependencies
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
# dependencies
DEPENDS+=	${PYPKGPREFIX}-flask-cors>=0:../../www/py-flask-cors
DEPENDS+=	${PYPKGPREFIX}-flask>=0:../../www/py-flask
DEPENDS+=	${PYPKGPREFIX}-alembic>=0:../../databases/py-alembic
DEPENDS+=	${PYPKGPREFIX}-cachetools>=0:../../devel/py-cachetools
DEPENDS+=	${PYPKGPREFIX}-click>=0:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-cloudpickle>=0:../../converters/py-cloudpickle
DEPENDS+=	${PYPKGPREFIX}-cryptography>=0:../../security/py-cryptography
DEPENDS+=	${PYPKGPREFIX}-databricks-sdk>=0:../../pkgsrc_myownpkgs/py-databricks-sdk
DEPENDS+=	${PYPKGPREFIX}-docker>=4.0.0:../../wip/py-docker
DEPENDS+=	${PYPKGPREFIX}-fastapi>=0:../../wip/py-fastapi
DEPENDS+=	${PYPKGPREFIX}-gitpython>=3.1.9:../../devel/py-gitpython
DEPENDS+=	${PYPKGPREFIX}-graphene>=0:../../wip/py-graphene
DEPENDS+=	${PYPKGPREFIX}-gunicorn>=0:../../www/py-gunicorn
DEPENDS+=	${PYPKGPREFIX}-huey>=2.5.0:../../pkgsrc_myownpkgs/py-huey
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=3.7.0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-opentelemetry-api>=0:../../pkgsrc_myownpkgs/py-opentelemetry-api
DEPENDS+=	${PYPKGPREFIX}-opentelemetry-proto>=0:../../pkgsrc_myownpkgs/py-opentelemetry-proto
DEPENDS+=	${PYPKGPREFIX}-opentelemetry-sdk>=0:../../pkgsrc_myownpkgs/py-opentelemetry-sdk
DEPENDS+=	${PYPKGPREFIX}-packaging>=0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-pandas>=0:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-protobuf>=3.12.0:../../devel/py-protobuf
DEPENDS+=	${PYPKGPREFIX}-apache-arrow>=4.0.0:../../pkgsrc_myownpkgs/py-apache-arrow
DEPENDS+=	${PYPKGPREFIX}-pydantic>=2.0.0:../../devel/py-pydantic
DEPENDS+=	${PYPKGPREFIX}-dotenv>=0.19.0:../../devel/py-dotenv
DEPENDS+=	${PYPKGPREFIX}-yaml>=5.1:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-requests>=2.17.3:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-sqlalchemy>=1.4.0:../../databases/py-sqlalchemy
DEPENDS+=	${PYPKGPREFIX}-sqlparse>=0.4.0:../../databases/py-sqlparse
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=4.0.0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-unicorn>=0:../../emulators/py-unicorn

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
