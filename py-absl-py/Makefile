# $NetBSD$

DISTNAME=	absl_py-2.4.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/absl_py/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/absl_py/
COMMENT=	Abseil Python Common Libraries
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-hatchling>=1.26:../../devel/py-hatchling

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
