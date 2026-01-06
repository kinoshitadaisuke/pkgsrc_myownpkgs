# $NetBSD$

DISTNAME=	opentelemetry_proto-1.39.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=o/opentelemetry_proto/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/opentelemetry_proto/
COMMENT=	OpenTelemetry Python Proto
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

# build dependencies
BUILD_DEPENDS+=	${PYPKGPREFIX}-hatchling>=0:../../devel/py-hatchling
# dependencies
DEPENDS+=	${PYPKGPREFIX}-protobuf>=5.0:../../devel/py-protobuf

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
