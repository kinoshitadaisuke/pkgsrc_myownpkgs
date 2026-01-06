# $NetBSD$

DISTNAME=	opentelemetry_sdk-1.39.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=o/opentelemetry_sdk/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/opentelemetry_sdk/
COMMENT=	OpenTelemetry Python SDK
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

# build dependencies
BUILD_DEPENDS+=	${PYPKGPREFIX}-hatchling>=0:../../devel/py-hatchling
# dependencies
DEPENDS+=	${PYPKGPREFIX}-opentelemetry-api>=1.39.0:../../pkgsrc_myownpkgs/py-opentelemetry-api
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=4.5.0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-opentelemetry-semantic-conventions>=0:../../pkgsrc_myownpkgs/py-opentelemetry-semantic-conventions

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
